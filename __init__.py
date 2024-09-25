import random

NODE_CATEGORY = "list-filter"
# TODO
# - Add pyproject.toml
#   - see https://docs.comfy.org/registry/overview

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
                "return_first_if_none": ("BOOLEAN", {"default": True, "tooltip": "Return the first image if the filtered list is empty."}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image_list",)
    OUTPUT_TOOLTIPS = ("The filtered list of images.",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True,)
    DESCRIPTION = "Filters the image list based on the provided index list."

    def run(self, image_list, index_list, return_first_if_none):
        return_first_if_none_bool = return_first_if_none[0]

        filtered_list = [image_list[i] for i in index_list if i < len(image_list)]
        if not filtered_list and return_first_if_none_bool:
            filtered_list = [image_list[0]] if image_list else []
        return (filtered_list,)

class FindAnyStrings:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_list": ("STRING", {"default": "", "tooltip": "The list of strings to search in."}),
                "search_strings": ("STRING", {"default": "", "tooltip": "The strings to search for."}),
                "delimiter": ("STRING", {"default": ",", "tooltip": "The delimiter used to split the search strings."}),
            }
        }

    RETURN_TYPES = ("INT", "STRING",)
    RETURN_NAMES = ("found_index_list", "found_string_list",)
    OUTPUT_TOOLTIPS = ("The list of indices where search strings are found.", "The list of found strings.",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True, True)
    DESCRIPTION = "Checks if any of the search strings are present in the string list."

    def run(self, string_list, search_strings, delimiter):
        search_strings_str = search_strings[0]
        delimiter_str = delimiter[0]

        search_list = [s.strip() for s in search_strings_str.split(delimiter_str)]
        found_indices = [i for i, s in enumerate(string_list) if any(search in s for search in search_list)]
        found_strings = [string_list[i] for i in found_indices]
        return (found_indices, found_strings)

class FindNotAnyStrings:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_list": ("STRING", {"default": "", "tooltip": "The list of strings to search in."}),
                "search_strings": ("STRING", {"default": "", "tooltip": "The list of strings to search for."}),
                "delimiter": ("STRING", {"default": ",", "tooltip": "The delimiter used to split the search strings."}),
            }
        }

    RETURN_TYPES = ("INT", "STRING",)
    RETURN_NAMES = ("not_found_index_list", "not_found_string_list",)
    OUTPUT_TOOLTIPS = ("The list of indices where search strings are not found.", "The list of strings where search strings are not found.",)
    FUNCTION = "run"
    CATEGORY = NODE_CATEGORY
    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (True, True)
    DESCRIPTION = "Checks if none of the search strings are present in the string list."

    def run(self, string_list, search_strings, delimiter):
        search_strings_str = search_strings[0]
        delimiter_str = delimiter[0]

        search_list = [s.strip() for s in search_strings_str.split(delimiter_str)]
        not_found_indices = [i for i, s in enumerate(string_list) if all(search not in s for search in search_list)]
        not_found_strings = [string_list[i] for i in not_found_indices]
        return (not_found_indices, not_found_strings)

class RandomNormalDist:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mean": ("FLOAT", {"default": 0.0, "tooltip": "The mean of the normal distribution."}),
                "std_dev": ("FLOAT", {"default": 1.0, "tooltip": "The standard deviation of the normal distribution."}),
                "num_samples": ("INT", {"default": 10, "tooltip": "The number of random samples to generate."}),
                "min_value": ("FLOAT", {"default": 5.0, "tooltip": "The minimum value of the generated samples."}),
                "max_value": ("FLOAT", {"default": 8.0, "tooltip": "The maximum value of the generated samples."}),
            }
        }

    RETURN_TYPES = ("LIST","FLOAT")
    RETURN_NAMES = ("random_samples","first_sample")
    OUTPUT_TOOLTIPS = ("The list of generated random samples.","The first generated random sample.")
    FUNCTION = "run"
    CATEGORY = "Random"
    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (True,False,)
    DESCRIPTION = "Generates random samples from a normal distribution."

    def run(self, mean, std_dev, num_samples, min_value, max_value):
        mean_val = mean
        std_dev_val = std_dev
        num_samples_val = num_samples
        min_val = min_value
        max_val = max_value

        random_samples = []
        for _ in range(num_samples_val):
            sample = random.gauss(mean_val, std_dev_val)
            sample = max(min(sample, max_val), min_val)
            sample = round(sample, 1)
            random_samples.append(sample)

        return (random_samples,random_samples[0],)

NODE_CLASS_MAPPINGS = {
    "list_filter_StringToIndex": StringToIndex,
    "list_filter_FilterStringListByIndexList": FilterStringListByIndexList,
    "list_filter_FilterImageListByIndexList": FilterImageListByIndexList,
    "list_filter_FindAnyStrings": FindAnyStrings,
    "list_filter_FindNotAnyStrings": FindNotAnyStrings,
    "random_normal_dist": RandomNormalDist,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "list_filter_StringToIndex": "Index List From String",
    "list_filter_FilterStringListByIndexList": "Filter String List",
    "list_filter_FilterImageListByIndexList": "Filter Image List",
    "list_filter_FindAnyStrings": "Find Any Strings",
    "list_filter_FindNotAnyStrings": "Find Not Any Strings",
    "random_normal_dist": "Random Normal Distribution",
}
