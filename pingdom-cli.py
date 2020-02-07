import json
import api

print('PINGDOM_CLI.....')
rawData = json.dumps(api.checks())
checkData = json.loads(rawData)

print('Total count: {0}'.format(checkData['counts']['total']))
print('Limited count: {0}'.format(checkData['counts']['limited']))
print('Filtered count: {0}'.format(checkData['counts']['filtered']))
print('Number of checks? {0}'.format(len(checkData['checks'])))

alerts = api.alerts()
print('ALERTS TEST')
print(alerts)
