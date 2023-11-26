from marshmallow import Schema, fields


class GoogleConfigSchema(Schema):
    id = fields.Int(dump_only=True, primary_key=True)
    app_id = fields.Str(required=True)
    google_account = fields.Str()
    google_campaign_id = fields.Str()
    skan_campaign_id = fields.Str()
    google_campaign_name = fields.Str()

