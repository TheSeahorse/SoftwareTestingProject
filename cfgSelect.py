def select(self, selector, namespaces=None, limit=None, **kwargs):
    if namespaces is None:
        namespaces = self._namespaces
    if limit is None:
        limit = 0
    if soupsieve is None:
        raise NotImplementedError(
            "Cannot execute CSS selectors because the soupsieve package is not installed."
        )
    results = soupsieve.select(selector, self, namespaces, limit, **kwargs)
    return ResultSet(None, results)












