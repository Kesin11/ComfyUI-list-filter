NODE_CATEGORY = "list-filter"

class StringToIndex:
  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "string": ("STRING", {"default": "", "tooltip": "The string to be split into indices."}),
        "delimiter": ("STRING", {"default": ",", "tooltip": "The delimiter used to split the string."}),
      }
    }

  RETURN_TYPES = ("INT",)
  RETURN_NAMES = ("index_list",)
  FUNCTION = "run"
  CATEGORY = NODE_CATEGORY
  INPUT_IS_LIST = False
  OUTPUT_IS_LIST = (True,)
  DESCRIPTION = "Splits a string into a list of indices based on the provided delimiter."

  def run(self, string, delimiter):
    return ([int(i) for i in string.split(delimiter)],)

class FilterStringListByIndexList:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_list": ("STRING", {"default": "", "tooltip": "The list of strings to be filtered."}),
                "index_list": ("INT", {"default": 0, "tooltip": "The list of indices to filter the string list."}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filtered_list",)
    OUTPUT_TOOLTIPS = ("The filtered list of strings.",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True,)
    DESCRIPTION = "Filters the string list based on the provided index list."

    def run(self, string_list, index_list):
        return ([string_list[i] for i in index_list if i < len(string_list)],)


class FilterImageListByIndexList:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_list": ("IMAGE", {"tooltip": "The list of images to be filtered."}),
                "index_list": ("INT", {"default": 0, "tooltip": "The list of indices to filter the image list."}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("filtered_list",)
    OUTPUT_TOOLTIPS = ("The filtered list of images.",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True,)
    DESCRIPTION = "Filters the image list based on the provided index list."

    def run(self, image_list, index_list):
        return ([image_list[i] for i in index_list if i < len(image_list)],)


class FindAnyStrings:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_list": ("STRING", {"default": "", "tooltip": "The list of strings to search in."}),
                "search_strings": ("STRING", {"default": "", "tooltip": "The list of strings to search for."}),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("found",)
    OUTPUT_TOOLTIPS = ("True if any search string is found, False otherwise.",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (False,)
    DESCRIPTION = "Checks if any of the search strings are present in the string list."

    def run(self, string_list, search_strings):
        return (any(s in string_list for s in search_strings),)


class FindNotAnyStrings:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_list": ("STRING", {"default": "", "tooltip": "The list of strings to search in."}),
                "search_strings": ("STRING", {"default": "", "tooltip": "The list of strings to search for."}),
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("not_found",)
    OUTPUT_TOOLTIPS = ("True if none of the search strings are found, False otherwise.",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (False,)
    DESCRIPTION = "Checks if none of the search strings are present in the string list."

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
