NODE_CATEGORY = "list-filter"

class StringToIndex:
  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "string": ("STRING", {"default": ""}),
        "delimiter": ("STRING", {"default": ","}),
      }
    }

  RETURN_TYPES = ("INT",)
  RETURN_NAMES = ("index_list",)
  FUNCTION = "run"
  CATEGORY = NODE_CATEGORY
  INPUT_IS_LIST = False
  OUTPUT_IS_LIST = (True,)

  def run(self, string, delimiter):
    return ([int(i) for i in string.split(delimiter)],)

class FilterStringListByIndexList:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_list": ("STRING", {"default": ""}),
                "index_list": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filtered_list",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True,)

    def run(self, string_list, index_list):
        return ([string_list[i] for i in index_list if i < len(string_list)],)


class FilterImageListByIndexList:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_list": ("IMAGE"),
                "index_list": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("filtered_list",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True,)

    def run(self, image_list, index_list):
        return ([image_list[i] for i in index_list if i < len(image_list)],)


class FindAnyStrings:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_list": ("STRING", {"default": ""}),
                "search_strings": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("found",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (False,)

    def run(self, string_list, search_strings):
        return (any(s in string_list for s in search_strings),)


class FindNotAnyStrings:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_list": ("STRING", {"default": ""}),
                "search_strings": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("not_found",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (False,)

    def run(self, string_list, search_strings):
        return (all(s not in string_list for s in search_strings),)


NODE_CLASS_MAPPINGS = {
    "list_filter_StringToIndex": StringToIndex,
    "list_filter_FilterStringListByIndexList": FilterStringListByIndexList,
    "list_filter_FilterImageListByIndexList": FilterImageListByIndexList,
    "list_filter_FindAnyStrings": FindAnyStrings,
    "list_filter_FindNotAnyStrings": FindNotAnyStrings,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "list_filter_StringToIndex": "Index List From String",
    "list_filter_FilterStringListByIndexList": "Filter String List",
    "list_filter_FilterImageListByIndexList": "Filter Image List",
    "list_filter_FindAnyStrings": "Find Any Strings",
    "list_filter_FindNotAnyStrings": "Find Not Any Strings",
}
