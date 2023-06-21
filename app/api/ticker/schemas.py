from marshmallow import Schema, fields, validate


class TickerSchema(Schema):
    id_ticker = fields.Int()
    ticker = fields.Str()
    price = fields.Float()
    timestamp = fields.Int()


class TickerRequestSchema(Schema):
    ticker = fields.Str(validate=validate.OneOf(["btc_usd", "eth_usd"]))


class ListTickerResponseSchema(Schema):
    tickers = fields.Nested(TickerSchema, many=True)


class PriceTickerResponseSchema(Schema):
    last_price = fields.Float()
