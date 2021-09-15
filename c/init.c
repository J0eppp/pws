#include <stdlib.h>
#include <jansson.h>
#include <string.h>

#include "types.h"

teacher_t *init_teachers(json_t *teachers_json, size_t len)
{
    size_t n_teachers = len;

    teacher_t *teachers = (teacher_t *)malloc(sizeof(teacher_t) * n_teachers);

    for (int i = 0; i < n_teachers; i++)
    {
        json_t *teacher_json;
        teacher_t teacher;

        teacher_json = json_array_get(teachers_json, i);

        const char *name = json_string_value(json_object_get(teacher_json, "name"));
        strcpy((char *)teacher.name, name);

        memcpy((teachers + i), &teacher, sizeof(teacher_t));
        free(teacher_json);
    }

    return teachers;
}

class_t *init_classes(json_t *classes_json, size_t len)
{
    class_t *classes = (class_t *)malloc(sizeof(class_t) * len);

    for (int i = 0; i < len; i++)
    {
        json_t *class_json;
        class_t class;

        class_json = json_array_get(classes_json, i);

        // Copy the name to the struct
        const char *name = json_string_value(json_object_get(class_json, "name"));
        strcpy((char *)class.name, name);

        printf("init: %s\n", class.name);

        // Copy the classes to the struct
        json_t *class_subjects_json = json_object_get(class_json, "subjects");
        for (int j = 0; j < json_array_size(class_subjects_json); j++)
        {
            char *name = (char *)json_string_value(json_array_get(class_subjects_json, j));
            if (strcmp(name, "WISKUNDE"))
            {
                class.subjects[j] = WISKUNDE;
                continue;
            }
            else if (strcmp(name, "ENGELS"))
            {
                class.subjects[j] = ENGELS;
                continue;
            }
            else if (strcmp(name, "NEDERLANDS"))
            {
                class.subjects[j] = NEDERLANDS;
                continue;
            }
            else if (strcmp(name, "GESCHIEDENIS"))
            {
                class.subjects[j] = GESCHIEDENIS;
                continue;
            }
            else if (strcmp(name, "FRANS"))
            {
                class.subjects[j] = FRANS;
                continue;
            }
            else if (strcmp(name, "DUITS"))
            {
                class.subjects[j] = DUITS;
                continue;
            }
            else if (strcmp(name, "AARDRIJKSKUNDE"))
            {
                class.subjects[j] = AARDRIJKSKUNDE;
                continue;
            }
            else if (strcmp(name, "NASK"))
            {
                class.subjects[j] = NASK;
                continue;
            }
            else
            {
                printf("ERROR invalid class: %s\n", name);
            }
        }

        memcpy(classes + i, &class, sizeof(class_t));

        free(class_json);
    }

    return classes;
}