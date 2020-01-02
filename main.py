from classes import Api, Meraki
import json, time, argparse, pprint


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--apiKey', required=False)
    parser.add_argument('--credentialsFile', required=False)

    args = parser.parse_args()

    apiKey = None

    if args.credentialsFile:
        with open(args.credentialsFile) as json_file:
            parsed = json.load(json_file)
            if "apiKey" in parsed:
                apiKey = parsed["apiKey"]

    if args.apiKey:
        apiKey = args.apiKey

    if apiKey == None:
        print('Please include a Cisco Meraki Dashboard API Key!')
        exit()


    meraki = Meraki(apiKey)

    orgs = meraki.getOrganisations()
    resultDevices = {}
    if len(orgs["data"]):
        for org in orgs["data"]:
            networks = meraki.getNetworks(org)
            if len(networks["data"]):
                for network in networks["data"]:
                    devices = meraki.getDevices(network)
                    for device in devices["data"]:
                        device["ports"] = {}
                        if device["pxType"] == 'switch':
                            resultDevices[device["mac"]] = device
                            ports = meraki.getSwitchPorts(device)
                            for port in ports["data"]:
                                port["inUse"] = False
                                resultDevices[device["mac"]]["ports"]["num" + str(port["number"])] = port
                            clients = meraki.getDeviceClients(device)
                            if clients["success"]:
                                for client in clients["data"]:
                                    if client["switchport"]:
                                         resultDevices[device["mac"]]["ports"]["num" + client["switchport"]]["inUse"] = True
    pprint.pprint(resultDevices)

if __name__ == '__main__':
    main()