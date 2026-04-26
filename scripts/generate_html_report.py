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

def generate_html(data):
    compliant = [x for x in data if x['status'] == 'COMPLIANT']
    non_compliant = [x for x in data if x['status'] != 'COMPLIANT']
    
    rows = ""
    for item in data:
        color = "#2ecc71" if item['status'] == "COMPLIANT" else "#e74c3c"
        icon = "✅" if item['status'] == "COMPLIANT" else "❌"
        rows += f"""
        <tr>
            <td>{icon} {item['rule']}</td>
            <td style="color:{color}; font-weight:bold">{item['status']}</td>
            <td>{item['timestamp']}</td>
        </tr>"""

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Compliance Report</title>
        <style>
            body {{ font-family: Arial; margin: 40px; background: #f5f5f5; }}
            h1 {{ color: #2c3e50; }}
            table {{ width: 100%; border-collapse: collapse; background: white; }}
            th {{ background: #2c3e50; color: white; padding: 12px; text-align: left; }}
            td {{ padding: 12px; border-bottom: 1px solid #ddd; }}
            .summary {{ display: flex; gap: 20px; margin: 20px 0; }}
            .card {{ padding: 20px; border-radius: 8px; color: white; min-width: 150px; text-align: center; }}
            .green {{ background: #2ecc71; }}
            .red {{ background: #e74c3c; }}
        </style>
    </head>
    <body>
        <h1>🔐 Compliance Report</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <div class="summary">
            <div class="card green"><h2>{len(compliant)}</h2><p>Compliant</p></div>
            <div class="card red"><h2>{len(non_compliant)}</h2><p>Non-Compliant</p></div>
        </div>
        <table>
            <tr><th>Rule</th><th>Status</th><th>Timestamp</th></tr>
            {rows}
        </table>
    </body>
    </html>"""

    filename = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    with open(filename, 'w') as f:
        f.write(html)
    print(f"✅ HTML Report saved to: {filename}")

if __name__ == "__main__":
    data = get_config_compliance()
    generate_html(data)
