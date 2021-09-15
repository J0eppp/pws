#include <stdlib.h>
#include <stdio.h>
#include <jansson.h>

#include "types.h"
#include "init.c"

void print_json(json_t *json)
{
    printf("%s\n", json_dumps(json, 0));
}

int main()
{
    // First we load all the JSON data
    json_t *json;
    json_error_t error;

    json = json_load_file("./data.json", 0, &error);
    if (!json)
    {
        printf("%s\n", error.text);
        return -1;
    }

    json_t *teachers_json = json_object_get(json, "teachers");
    size_t n_teachers = json_array_size(teachers_json);
    json_t *classes_json = json_object_get(json, "classes");
    size_t n_classes = json_array_size(classes_json);

    teacher_t *teachers = (teacher_t *)malloc(sizeof(teacher_t) * n_teachers);
    teachers = init_teachers(teachers_json, n_teachers);

    class_t *classes = (class_t *)malloc(sizeof(class_t) * n_classes);
    classes = init_classes(classes_json, n_classes);

    for (int i = 0; i < n_classes; i++)
    {
        class_t class = *(classes + i);
        // char name[16] = class.name;

        for (int j = 0; j < 32; j++)
        {
            char *subject = subject_to_string(class.subjects[j]);
            printf("%s => %s\n", class.name, subject);
        }
    }

    // for (int i = 0; i < n_teachers; i++)
    // {
    //     teacher_t teacher = *(teachers + i);
    //     // Do smth with the teachers?
    //     // printf("%s\n", teacher.name);
    // }

    free(teachers);
    return 0;
}
