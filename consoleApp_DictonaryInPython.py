
print(" __C O N S O L E  A P P__")
print("__________________________")
print("Top 50 Abbreviations in CS")
print("-------------------------")


generate=str(input("Press any key to genreate all abreviations: "))







CS_Abreviations={

    "A/D":"Analog-to-Digital",
    "AI":"Artificial Intelligence",
    "ALGOL":"Algorithic Language",
    "BIOS":"Basic Inpute Output System",
    "CD-ROM":"Compact Disk Read Only Memory",
    "CD-RW":"CD Read/Write",
    "CL":"Command Language",
    "CPU":"Central Processing Unit",
    "DBMS":"Data Base Management System",
    "DNA":"Digital Network Architecture",
    "DRAM":"Dynamic RAM",
    "DVD":"Digital Video/Versatile Disk",
    "ENIAC":"Electronic Numerical Integrator And Calculator",
    "WWW":"World Wide Web",
    "WORM":"Write Once Read Many",
    "WLAN":"Wireless Local Area Network",
    "WAN":"	Wide Area Network",
    "UTF":"Unicode Transformation Format",
    "URL":"Uniform Resource Locator",
    "UDP":"User Datagram Protocol",
    "TCP":"Transport Control Protocol",
    "TB":"Tera Bytes",
    "SSI":"Small Scale Integration",
    "SRAM":"Static RAM",
    "SQL":"Structured Query Language",
    "ROM":"Read Only Memory",
    "RAM":"Random Access Memory",
    "XML":"eXtensible Markup Language",
    "XHTML":"eXtensible HyperText Markup Language",
    "WLL":"Wireless Local Loop",
    "WiMAX":"Worldwide Interoperability for Microwave Access",
    "VoIP":"Voice over Internet Protocol",
    "VOD":"Video-On-Demand",
    "VGA":"Video Graphics Array",
    "VDT":"Video Display Terminal",
    "VCR":"Video Cassette Recorder",
    "VAN":"Value Added Network",
    "ULSI":"Ultra Large Scale Integration",
    "TDM":"Time Division Multiplexing",
    "SDLC":"Software Development Life Cycle",
    "PIP":"Peripheral Interchange Program",
    "PDP":"Program Data Processor",
    "PDF":"Portable Document Format",
    "PDL":"Program Design Language",
    "PC":"Personal Computer",
    "OSS":"Open Source Software",
    "OSI":"Open System Interconnection",
    "OMR":"Optical Mark Reader",
    "MPEG":"Moving Pictures Experts Group",
    "MNP":"Microcom Network Protocol",
}

if generate:

    print("List of All Abreviations")
    print("-------------------------")
    i=1
    for state in CS_Abreviations:
        print(i,state)
        i+=1
    print("-------------------------")


user_input=-1


while user_input != 0:

    print("To Exit the Appliction, please Enter 0")
    print("....................................")
    user_input=int(input("Enter a number to know about its associated Abbreviation:" ))



    if user_input == 1:
        print(CS_Abreviations["A/D"])

    elif user_input == 2:
        print(CS_Abreviations["AI"])

    elif user_input == 3:
        print(CS_Abreviations["ALGOL"])

    elif user_input == 4:
        print(CS_Abreviations["BIOS"])

    elif user_input == 5:
        print(CS_Abreviations["CD-ROM"])

    elif user_input == 6:
        print(CS_Abreviations["CD-RW"])

    elif user_input == 7:
        print(CS_Abreviations["CL"])

    elif user_input == 8:
        print(CS_Abreviations["CPU"])

    elif user_input == 9:
        print(CS_Abreviations["DBMS"])

    elif user_input == 10:
        print(CS_Abreviations["DNA"])

    elif user_input == 11:
        print(CS_Abreviations["DRAM"])

    elif user_input == 12:
        print(CS_Abreviations["DVD"])

    elif user_input == 13:
        print(CS_Abreviations["ENIAC"])

    elif user_input == 14:
        print(CS_Abreviations["WWW"])

    elif user_input == 15:
        print(CS_Abreviations["WORM"])

    elif user_input == 16:
        print(CS_Abreviations["WLAN"])

    elif user_input == 17:
        print(CS_Abreviations["WAN"])

    elif user_input == 18:
        print(CS_Abreviations["UTF"])

    elif user_input == 19:
        print(CS_Abreviations["URL"])

    elif user_input == 20:
        print(CS_Abreviations["UDP"])

    elif user_input == 21:
        print(CS_Abreviations["TCP"])

    elif user_input == 22:
        print(CS_Abreviations["TB"])

    elif user_input == 23:
        print(CS_Abreviations["SSI"])

    elif user_input == 24:
        print(CS_Abreviations["SRAM"])

    elif user_input == 25:
        print(CS_Abreviations["SQL"])

    elif user_input == 26:
        print(CS_Abreviations["ROM"])

    elif user_input == 27:
        print(CS_Abreviations["RAM"])

    elif user_input == 28:
        print(CS_Abreviations["XML"])

    elif user_input == 29:
        print(CS_Abreviations["XHTML"])

    elif user_input == 30:
        print(CS_Abreviations["WLL"])

    elif user_input == 31:
        print(CS_Abreviations["WiMAX"])

    elif user_input == 32:
        print(CS_Abreviations["VoIP"])

    elif user_input == 33:
        print(CS_Abreviations["VOD"])

    elif user_input == 34:
        print(CS_Abreviations["VGA"])

    elif user_input == 35:
        print(CS_Abreviations["VDT"])

    elif user_input == 36:
        print(CS_Abreviations["VCR"])

    elif user_input == 37:
        print(CS_Abreviations["VAN"])

    elif user_input == 38:
        print(CS_Abreviations["ULSI"])

    elif user_input == 39:
        print(CS_Abreviations["TDM"])

    elif user_input == 40:
        print(CS_Abreviations["SDLC"])

    elif user_input == 41:
        print(CS_Abreviations["PIP"])

    elif user_input == 42:
        print(CS_Abreviations["PDP"])


    elif user_input == 43:
        print(CS_Abreviations["PDF"])

    elif user_input == 44:
        print(CS_Abreviations["PDL"])

    elif user_input == 45:
        print(CS_Abreviations["PC"])

    elif user_input == 46:
        print(CS_Abreviations["OSS"])

    elif user_input == 47:
        print(CS_Abreviations["OSI"])

    elif user_input == 48:
        print(CS_Abreviations["OMR"])

    elif user_input == 49:
        print(CS_Abreviations["MPEG"])

    elif user_input == 50:
        print(CS_Abreviations["MNP"])


print("Happy Coding!")


print("Program Terminated")
