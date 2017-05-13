import colander


class BodySchema(colander.MappingSchema):
    id = colander.SchemaNode(colander.String(), missing=colander.required)


class QuerySchema(colander.MappingSchema):
    foo = colander.SchemaNode(colander.String(), validator=colander.Length(3),
                              missing=colander.drop)


class HeaderSchema(colander.MappingSchema):
    bar = colander.SchemaNode(colander.String(), missing=colander.drop)


class GetRequestSchema(colander.MappingSchema):
    querystring = QuerySchema()


class PutRequestSchema(colander.MappingSchema):
    body = BodySchema()
    querystring = QuerySchema()
    header = HeaderSchema()
