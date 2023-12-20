from marshmallow import Schema, fields


class GoogleTokensSchemaPost(Schema):
    id = fields.Int(dump_only=True)
    app_id = fields.Str(required=True)
    network_user_id = fields.Str(required=True)
    long_live_token = fields.Str(required=True)
