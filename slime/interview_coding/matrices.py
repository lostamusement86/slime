# ######################################################################### #
# rotate an image represented by a matrix (This is also known as a bitmap.) #
# This is a common interview question by the big 3                          #
# ######################################################################### #


def rotateImage(a):
    # Declare a list to hold the rotated vectors
    new_a = []

    for i in range(len(a[0])):
        new_list = []  # Create an empty vector
        for j in reversed(range(len(a))):  # Reversing here is important to match the desired rotation
            new_list.append(a[j][i])  # append the elements to the vector in the proper order
        new_a.append(new_list)  # add the new vector into the new list
    return new_a  # return the rotated bitmap


