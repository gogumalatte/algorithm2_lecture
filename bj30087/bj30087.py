n = int(input())
for _ in range(n):
    semina_name = input()
    match(semina_name):
        case "Algorithm":
            print("204")
        case "DataAnalysis":
            print("207")
        case "ArtificialIntelligence":
            print("302")
        case "CyberSecurity":
            print("B101")
        case "Network":
            print("303")
        case "Startup":
            print("501")
        case "TestStrategy":
            print("105")