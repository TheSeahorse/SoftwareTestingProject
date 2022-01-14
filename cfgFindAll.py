    def find_all(self, name=None, attrs={}, recursive=True, text=None,
                 limit=None, **kwargs):
        generator = self.descendants
        if not recursive:
            generator = self.children
        return self._find_all(name, attrs, text, limit, generator, **kwargs)
        findAll = find_all  # BS3
        findChildren = find_all  # BS2

    def _find_all(self, name, attrs, text, limit, generator, **kwargs):
        if text is None and 'string' in kwargs:
            text = kwargs['string']
            del kwargs['string']
        if isinstance(name, SoupStrainer):
            strainer = name
        else:
            strainer = SoupStrainer(name, attrs, text, **kwargs)
        if text is None and not limit and not attrs and not kwargs:
            if name is True or name is None:
                result = (element for element in generator
                          if isinstance(element, Tag))
                return ResultSet(strainer, result)
            elif isinstance(name, str):
                # Optimization to find all tags with a given name.
                if name.count(':') == 1:
                    prefix, local_name = name.split(':', 1)
                else:
                    prefix = None
                    local_name = name
                result = (element for element in generator
                          if isinstance(element, Tag)
                          and (
                              element.name == name
                          ) or (
                              element.name == local_name
                              and (prefix is None or element.prefix == prefix)
                          )
                )
                return ResultSet(strainer, result)
        results = ResultSet(strainer)
        while True:
            try:
                i = next(generator)
            except StopIteration:
                break
            if i:
                found = strainer.search(i)
                if found:
                    results.append(found)
                    if limit and len(results) >= limit:
                        break
        return results
