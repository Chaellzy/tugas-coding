def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    
    if n == 1:
        return arr

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return bubble_sort_recursive(arr, n - 1)

if __name__ == "__main__":
    try:
        array = list(map(int, input("Masukkan elemen-elemen list (pisahkan dengan spasi): ").split()))
        print("List Sebelum Disorting:", array)
        sorted_array = bubble_sort_recursive(array)
        print("List Setelah Disorting:", sorted_array)
    except ValueError:
        print("Input tidak valid! Pastikan Anda memasukkan angka saja.")
