import pandas as pd
import urllib3
from swat import CAS
from auth_utils import get_token, connect_cas_https

# Suppress SSL warnings for demo
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    token = get_token()

    # Connect to CAS using the proper OAuth method
    cas = connect_cas_https(token)

    # Create sample data for demonstration
    sample_data = pd.DataFrame({
        'Weight': [3000, 3500, 4000, 2500, 3200, 3800, 2800, 3600, 4200, 2900],
        'MPG_City': [25, 22, 18, 30, 24, 16, 28, 20, 15, 26],
        'Make': ['Toyota', 'Honda', 'Ford', 'Nissan', 'Chevy', 'Dodge', 'Mazda', 'BMW', 'Mercedes', 'Hyundai'],
        'Model': ['Camry', 'Accord', 'F150', 'Altima', 'Malibu', 'Charger', '3', 'X3', 'GLE', 'Sonata']
    })

    # Drop the table if it exists, then upload the data to CAS
    try:
        cas.table.droptable(caslib="CASUSER", name="cars")
    except:
        pass  # Table doesn't exist, which is fine
    
    cas.upload(sample_data, casout={"name":"cars", "promote":True})

    # Convert to SWAT CASTable
    tbl = cas.CASTable("cars")

    # Build a linear model: predict MPG_City from Weight
    cas.loadactionset('regression')
    result = cas.regression.glm(
        table={"name":"cars"},
        inputs=["Weight"],
        target="MPG_City"
    )

    # Print the results
    print("\nGLM Model Results:")
    print(result)

    # Get parameter estimates from the result
    if 'ParameterEstimates' in result:
        estimates = result['ParameterEstimates']
        print("\nParameter Estimates:")
        print(estimates)
        
        # Extract intercept and coefficient
        intercept = estimates[estimates['Parameter'] == 'Intercept']['Estimate'].iloc[0]
        weight_coef = estimates[estimates['Parameter'] == 'Weight']['Estimate'].iloc[0]
        
        print(f"\nModel Equation: MPG_City = {intercept:.3f} + {weight_coef:.6f} * Weight")
        print(f"Interpretation: For every 1 pound increase in weight, MPG_City decreases by {abs(weight_coef):.6f}")
        
    else:
        print("\nParameter estimates not available in this format")
        print("Available result keys:", list(result.keys()))

    print("\nModel successfully built and analyzed!")

    # Close the CAS connection
    cas.close()


if __name__ == '__main__':
    main()
