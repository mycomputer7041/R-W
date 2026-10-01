# class book:

#     def __init__(self):
#         self.__title=""
#         self.__auther=""

# ૧. 3D List બનાવવું (2 બ્લોક/લેયર, જેમાં દરેકની અંદર 2 રો અને 3 કોલમ છે)
list3d = [
    [ [1, 2, 3], [4, 5, 6] ],       # Layer 0
    [ [7, 8, 9], [10, 11, 12] ]     # Layer 1
]

print("\n--- 3D List ---")
print("આખો ડેટા:", list3d)

# ૨. ડેટા ઍક્સેસ કરવો [Layer][Row][Column]
# Layer 1, Row 0, Column 2 નો એલિમેન્ટ:
print("Layer 1, Row 0, Column 2 નો ડેટા:", list3d[1][0][2])  # 9

# ૩. Nested Loops વડે 3D ડેટા પ્રિન્ટ કરવો
print("\n3D Data print:")
for layer in list3d:
    for row in layer:
        print(row)
    print()
