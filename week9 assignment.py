def decode_packet(packet_string, required_fields):
    if packet_string[-1] != ';':
        return ("Error: Invalid packet format.")

    cleaned_packet = packet_string[:-1]
    kv_pairs = cleaned_packet.split("|")
    extracted_keys = []
    extracted_values = []

    for pair in kv_pairs:
        if ':' in pair:
            parts = pair.split(':')
            key = parts[0].strip()
            value = parts[1].strip()

            if key:
                extracted_keys.append(key)
                extracted_values.append(value)

    missing_fields = []
    for required_key in required_fields:
        if required_key not in extracted_keys:
            missing_fields.append(required_key)

    if len(missing_fields) > 0:
        quoted_fields = []
        for field in missing_fields:
            quoted_fields.append(f"'{field}'") 
        fields_string = ", ".join(quoted_fields)
        error_message = (f"Error: Missing required fields: [{fields_string}]")
        return error_message
    
    final_values = []
    for required_key in required_fields:
        key_index = extracted_keys.index(required_key)
        value = extracted_values[key_index]
        final_values.append(value)

    return final_values


packet1 = "ID:A45F|STATUS:OK|PAYLOAD:Data123|CHECKSUM:XYZ;"
required1 = ["ID", "STATUS", "PAYLOAD"]
print(decode_packet(packet1, required1))

packet2 = "ID:B98C|STATUS:PENDING;"
required2 = ["ID", "STATUS", "PAYLOAD"]
print(decode_packet(packet2, required2))

packet3 = "ID:C12D|STATUS:ERROR"
required3 = ["ID"]
print(decode_packet(packet3, required3))

packet4 = "PAYLOAD:MoreData|STATUS:OK|ID:D45E;"
required4 = ["ID", "STATUS", "PAYLOAD"]
print(decode_packet(packet4, required4))
