from marshmallow import Schema, fields


class Oauth2SchemaPost(Schema):
    id = fields.Int(dump_only=True)
    client_id = fields.Str(required=True)
    refresh_token = fields.Str(required=True)
    client_secret = fields.Str(required=False, default='test-client-value')
    grant_type = fields.Str(required=False, default='refresh_token')
