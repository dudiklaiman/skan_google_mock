from marshmallow import Schema, fields


class ValuesSchema(Schema):
    # default true
    skAdNetworkAttributionCredit = fields.Str(required=False, default=True)
    # default new installer
    skAdNetworkUserType = fields.Str(required=False, default="NEW_INSTALLER")
    # default value 0
    skAdNetworkPostbackSequenceIndex = fields.Str(required=False, default="0")
    # default UNAVAILABLE
    skAdNetworkSourceType = fields.Str(required=False, default="UNAVAILABLE")
    # default INTERACTION
    skAdNetworkAdEventType = fields.Str(required=False, default="INTERACTION")
    # default campaign id
    campaign_name = fields.Str(required=True)

    skAdNetworkTotalConversions = fields.Str(required=True)
    # default total conversion
    skAdNetworkInstalls = fields.Str(required=False, default=skAdNetworkTotalConversions)


class GoogleConfigSchemaGet(Schema):
    app_id = fields.Str(required=False)
    network_user_id = fields.Str(required=False)
    customer_id = fields.Str(required=False)
    customer_client = fields.Str(required=False)
    campaign_id = fields.Str(required=False)


class GoogleConfigSchemaPost(ValuesSchema):
    # consider to remove
    id = fields.Int(dump_only=True)
    app_id = fields.Str(required=True)
    network_user_id = fields.Str(required=True)
    # default value is value app id
    customer_id = fields.Str(required=False, default=network_user_id)
    # default value network user id
    customer_client = fields.Str(required=False, default=app_id)
    # default app id + network user id
    campaign_id = fields.Str(required=False, default=f"{network_user_id}{app_id}")


class GoogleConfigSchemaPut(ValuesSchema):
    app_id = fields.Str(required=True)
    network_user_id = fields.Str(required=True)
    customer_id = fields.Str(required=True)
    customer_client = fields.Str(required=True)
    campaign_id = fields.Str(required=True)


class GoogleConfigSchemaDelete(Schema):
    app_id = fields.Str(required=True)
    network_user_id = fields.Str(required=True)
    customer_id = fields.Str(required=True)
    customer_client = fields.Str(required=True)
    bucket_id = fields.Str(required=True)
