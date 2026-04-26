import boto3
import json
from datetime import datetime

def get_config_compliance():
    client = boto3.client('config', region_name='us-east-1')
    response = client.describe_compliance_by_config_rule()
    results = []
    for rule in response['ComplianceByConfigRules']:
        results.append({
            'rule': rule['ConfigRuleName'],
            'status': rule['Compliance']['ComplianceType'],
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    return results

def generate_report(data):
    print("\n=============================")
    print("  COMPLIANCE REPORT")
    print(f"  Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=============================\n")
    for item in data:
        status = "✅ COMPLIANT" if item['status'] == "COMPLIANT" else "❌ NON_COMPLIANT"
        print(f"{status} — {item['rule']}")
    print("\n=============================\n")

def save_evidence(data):
    filename = f"reports/evidence_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"✅ Evidence saved to: {filename}")

if __name__ == "__main__":
    data = get_config_compliance()
    generate_report(data)
    save_evidence(data)
