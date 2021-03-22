def values_conversion(data):
    for key in data:
        updated_data = [time for time in data[key]]
        it = iter(updated_data)
        data[key] = sorted(list(zip(it, it)))
    return data


def inner_intersections_remove(intervals):
    index = 0
    updated_intervals = intervals
    while (index + 1) < len(updated_intervals):
        max_start = max([updated_intervals[index][0], updated_intervals[index+1][0]])
        min_end = min([updated_intervals[index][1], updated_intervals[index+1][1]])
        if (min_end - max_start) >= 0:
            start = min([updated_intervals[index][0], updated_intervals[index+1][0]])
            end = max([updated_intervals[index][1], updated_intervals[index+1][1]])
            updated_intervals = updated_intervals[:index] + [(start, end)] + updated_intervals[index+2:] 
        else:
            index = index + 1
    return updated_intervals


def outer_intersections(data_key_one, data_key_two):
    result = []
    for pupil_couple in data_key_one:
        for tutor_couple in data_key_two:
            pupil_start, tutor_start = pupil_couple[0], tutor_couple[0]
            pupil_end, tutor_end = pupil_couple[1], tutor_couple[1]
            if (pupil_start <= tutor_end and
                tutor_start <= pupil_end):
                start = max(pupil_start, tutor_start)
                end = min(pupil_end, tutor_end)
                result.append((start, end))
    return result


def appearance(data):
    data = values_conversion(data)
    for intervals in data:
        data[intervals] = inner_intersections_remove(data[intervals])
    pupil_tutor_intersections = outer_intersections(data['pupil'], data['tutor'])
    if pupil_tutor_intersections:
        lesson_intersections = outer_intersections(data['lesson'], pupil_tutor_intersections)
    differences = [(couple[1] - couple[0]) for couple in lesson_intersections]
    return sum(differences)


tests = [
    {
    'data': 
            {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
            },
    'answer': 3117
    },

    {
    'data': 
            {
            'lesson': [1594702800, 1594706400],
            'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
            'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]
            },
    'answer': 3577
    },

    {
    'data': {
            'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
            'tutor': [1594692017, 1594692066, 1594692068, 1594696341]
            },
    'answer': 3565
    },
   
]


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'