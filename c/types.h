#ifndef TYPES_H
#define TYPES_H

// Predefine everything
typedef struct teacher_s teacher_t;
typedef struct lesson_s lesson_t;
typedef struct class_s class_t;

typedef enum subject_s subject_t;

typedef enum subject_s
{
    WISKUNDE,
    ENGELS,
    NEDERLANDS,
    GESCHIEDENIS,
    FRANS,
    DUITS,
    AARDRIJKSKUNDE,
    NASK,
} subject_t;

static inline char *subject_to_string(subject_t s)
{
    static char *strings[] = {"WISKUNDE", "ENGELS", "NEDERLANDS", "GESCHIEDENIS", "FRANS", "DUITS", "AARDRIJKSKUNDE", "NASK" /* continue for rest of values */};

    return strings[s];
}

typedef struct lesson_s
{
    subject_t subject;
    teacher_t *teacher;
    uint hour;
} lesson_t;

typedef struct teacher_s
{
    char name[128];    // Cannot do this with a pointer, idk why, it gives a segfault
    subject_t subject; // Assuming a teacher can only teach one subject for now
    size_t n_lessons;
    lesson_t *lessons;
} teacher_t;

typedef struct class_s
{
    char name[16];
    // subject_t *subjects;
    // uint subjects_len;
    subject_t subjects[32];

    lesson_t *lessons;
    uint lessons_len;
} class_t;

#endif