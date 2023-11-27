from marshmallow import Schema, fields


class ValuesSchema(Schema):
    skan_campaign_id = fields.Str(required=False)
    google_campaign_name = fields.Str(required=False)
    is_skadnetwork_attribution = fields.Str(required=False)
    total_postbacks = fields.Str(required=False)
    skan_conversion_id = fields.Str(required=False)
    postback_start_date = fields.Str(required=False)
    postback_duration = fields.Str(required=False)
    skan_click = fields.Str(required=False)
    skan_view = fields.Str(required=False)
    is_conversion_id_modeled = fields.Str(required=False)
    coarse_conversion_value = fields.Str(required=False)
    postback_sequence_index = fields.Str(required=False)
    hsid = fields.Str(required=False)
    redownload = fields.Str(required=False)
    skan_version = fields.Str(required=False)
    fidelity_type = fields.Str(required=False)


class GoogleConfigSchemaGet(Schema):
    app_id = fields.Str(required=False)
    google_account = fields.Str(required=False)
    google_campaign_id = fields.Str(required=False)


class GoogleConfigSchemaPost(ValuesSchema):
    id = fields.Int(dump_only=True)
    app_id = fields.Str(required=True)
    google_account = fields.Str(required=False)
    google_campaign_id = fields.Str(required=False)


class GoogleConfigSchemaPut(ValuesSchema):
    app_id = fields.Str(required=True)
    google_account = fields.Str(required=True)
    google_campaign_id = fields.Str(required=True)


class GoogleConfigSchemaDelete(Schema):
    id = fields.Int(dump_only=True)
    app_id = fields.Str(required=True)
    google_account = fields.Str()
    google_campaign_id = fields.Str()
