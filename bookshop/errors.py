class BookshopException(Exception):
    pass


class ModelException(BookshopException):
    pass


class RecordNotFound(ModelException):
    def __init__(self, model_cls, query):
        self.model_cls = model_cls
        self.query = query
        self.msg = f"could not find {model_cls.__name__.lower()} with query {query}"
        self.error_type = "record_not_found"
        super().__init__(self.msg)


class ValidationError(ModelException):
    def __init__(self, err):
        self.parent_err = err
        self.msg = ";".join(err.messages)
        self.error_type = "validation_error"
        super().__init__(self.msg)


class FilterException(BookshopException):
    pass


class ViewException(BookshopException):
    pass
