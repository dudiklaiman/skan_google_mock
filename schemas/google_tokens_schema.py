from marshmallow import Schema, fields


class GoogleTokenSchema(Schema):
    id = fields.Int(dump_only=True, primary_key=True)
    app_id = fields.Str(required=True)
    access_token = fields.Str(required=True)

