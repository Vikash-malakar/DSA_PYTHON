def find_median_sorted_arrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    mid = n // 2

    if n % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2
    else:
        return float(merged[mid])


if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    print(f"Array 1: {nums1} | Array 2: {nums2}")
    print(f"Median: {find_median_sorted_arrays(nums1, nums2)}\n")

    nums1_even = [1, 2]
    nums2_even = [3, 4]
    print(f"Array 1: {nums1_even} | Array 2: {nums2_even}")
    print(f"Median: {find_median_sorted_arrays(nums1_even, nums2_even)}")