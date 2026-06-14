import json

# Load method_out.json
with open('method_out.json', 'r') as f:
    data = json.load(f)

print('Adding predict_* fields...')

# Add predict_* fields to each example
for dataset in data.get('datasets', []):
    for example in dataset.get('examples', []):
        method = example.get('metadata_method', '')
        
        try:
            output = json.loads(example['output'])
            
            if method == 'system_gmm' and 'coefficients' in output:
                coef = output['coefficients'].get('L1_gini', None)
                example['predict_system_gmm'] = f"GMM coef: {coef:.4f}" if coef else "GMM: no coef"
            elif method == 'iv_estimation' and 'coefficients' in output:
                coef = output['coefficients'].get('gini', 
                              output['coefficients'].get('gini_hat', None))
                example['predict_iv_estimation'] = f"IV coef: {coef:.4f}" if coef else "IV: no coef"
            elif method == 'mediation_analysis' and 'effects' in output:
                indirect = output['effects'].get('indirect', {}).get('coefficient', None)
                example['predict_mediation'] = f"Indirect: {indirect:.4f}" if indirect else "Mediation: no effect"
            elif method == 'specification_curve' and 'median_coefficient' in output:
                example['predict_specification_curve'] = f"Median: {output['median_coefficient']:.4f}"
        except:
            pass
        
        # Ensure at least one predict_* field
        if not any(k.startswith('predict_') for k in example.keys()):
            example['predict_method'] = "Not available"

# Save
with open('method_out.json', 'w') as f:
    json.dump(data, f, indent=2)

print('Saved updated method_out.json')

# Verify
predict_count = 0
total = 0
for dataset in data.get('datasets', []):
    for example in dataset.get('examples', []):
        total += 1
        if any(k.startswith('predict_') for k in example.keys()):
            predict_count += 1
            
print(f'Examples with predict_* fields: {predict_count}/{total}')
