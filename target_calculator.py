import json

def calculate_sum_of_products(list1,list2):
        sum_of_products = 0
        for index in range(len(list1)):
            product = list1[index] * list2[index]
            sum_of_products += product
        return sum_of_products

def calculate_term_mark(term_marks, term_weights):
    sum_weights = sum(term_weights)
    new_weights = [weight / sum_weights for weight in term_weights]

    return calculate_sum_of_products(term_marks, new_weights)

def calculate_target_exam_mark(weighted_sum,exam_weight,course_target):
    return (course_target - weighted_sum) / exam_weight

if __name__=="__main__":
    course_file_name = input( \
        "Type in the file name (file must be in the same folder as this script):")

    course_file = open(course_file_name)

    course_data = json.loads(course_file.read())
    
    weighted_sum = calculate_sum_of_products(course_data["term_marks"], \
                    course_data["term_weights"])

    target_exam_mark = calculate_target_exam_mark(weighted_sum, \
                    course_data["exam_weight"], course_data["course_target"])

    term_mark = calculate_term_mark(course_data["term_marks"], \
                course_data["term_weights"])

    print("Your term mark is", term_mark)

    print("Your target exam mark is", target_exam_mark)
