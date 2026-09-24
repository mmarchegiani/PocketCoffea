from coffea.nanoevents import NanoAODSchema, DelphesSchema

def get_schema(schema_name: str):
    if schema_name == "NanoAODSchema":
        return NanoAODSchema
    elif schema_name == "DelphesSchema":
        return DelphesSchema
    else:
        raise ValueError(f"Unknown schema name: {schema_name}. Supported schemas are 'NanoAODSchema' and 'DelphesSchema'.")

def get_treename(schema_name: str):
    if schema_name == "NanoAODSchema":
        return "Events"
    elif schema_name == "DelphesSchema":
        return "Delphes"
    else:
        raise ValueError(f"Unknown schema name: {schema_name}. Supported schemas are 'NanoAODSchema' and 'DelphesSchema'.")
