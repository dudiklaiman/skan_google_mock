from marshmallow import Schema, fields


class GoogleTokensSchemaPost(Schema):
    id = fields.Int(dump_only=True)
    app_id = fields.Str(required=True)
    access_token = fields.Str(required=True)


class GoogleTokensSchemaGet(Schema):
    id = fields.Int(dump_only=True)
    app_id = fields.Str()
    access_token = fields.Str()

