#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

struct node *start = NULL, *p, *temp, *prev, *temp1;

void create() {
    int n, i, e;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++) {
        printf("Enter element: ");
        scanf("%d", &e);
        p = (struct node *)malloc(sizeof(struct node));
        p->data = e;
        p->next = NULL;
        if (start == NULL) {
            start = p;
            p->next = start;
        } else {
            temp = start;
            while (temp->next != start) {
                temp = temp->next;
            }
            temp->next = p;
            p->next = start;
        }
    }
}

void display() {
    if (start == NULL) {
        printf("List is empty");
    } else {
        temp = start;
        do {
            printf("%d ", temp->data);
            temp = temp->next;
        } while (temp != start);
    }
}

void insertbeg() {
    int e;
    p = (struct node *)malloc(sizeof(struct node));
    printf("Enter element to be inserted: ");
    scanf("%d", &e);
    p->data = e;
    p->next = NULL;
    if (start == NULL) {
        start = p;
        p->next = start;
    } else {
        temp = start;
        while (temp->next != start) {
            temp = temp->next;
        }
        p->next = start;
        temp->next = p;
        start = p;
    }
}

void insertend() {
    int e;
    p = (struct node *)malloc(sizeof(struct node));
    printf("Enter element to be inserted: ");
    scanf("%d", &e);
    p->data = e;
    p->next = NULL;
    if (start == NULL) {
        start = p;
        p->next = start;
    } else {
        temp = start;
        while (temp->next != start) {
            temp = temp->next;
        }
        temp->next = p;
        p->next = start;
    }
}

void insertpos() {
    int i = 1, e, pos;
    p = (struct node *)malloc(sizeof(struct node));
    printf("Enter element to be inserted: ");
    scanf("%d", &e);
    printf("Enter position: ");
    scanf("%d", &pos);
    p->data = e;
    p->next = NULL;
    temp = start;
    while (i < pos) {
        prev = temp;
        temp = temp->next;
        i++;
    }
    prev->next = p;
    p->next = temp;
}

void delbeg() {
    if (start == NULL) {
        printf("List is empty");
    } else {
        temp = start;
        while (temp->next != start) {
            temp = temp->next;
        }
        temp->next = start->next;
        free(start);
        start = temp->next;
    }
}

void delend() {
    if (start == NULL) {
        printf("List is empty");
    } else {
        temp = start;
        while (temp->next != start) {
            prev = temp;
            temp = temp->next;
        }
        prev->next = start;
        free(temp);
    }
}

void delpos() {
    int pos, i;
    if (start == NULL) {
        printf("List is empty");
    } else {
        printf("Enter position to delete: ");
        scanf("%d", &pos);
        temp = start;
        for (i = 1; i < pos; i++) {
            prev = temp;
            temp = temp->next;
        }
        prev->next = temp->next;
        free(temp);
    }
}

int main() {
    int choice;
    while (1) {
        printf("Select choice:\n");
        printf("1. Create\n");
        printf("2. Display\n");
        printf("3. Insert at beginning\n");
        printf("4. Insert at end\n");
        printf("5. Insert at position\n");
        printf("6. Delete at beginning\n");
        printf("7. Delete at end\n");
        printf("8. Delete at position\n");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                create();
                break;
            case 2:
                display();
                break;
            case 3:
                insertbeg();
                break;
            case 4:
                insertend();
                break;
            case 5:
                insertpos();
                break;
            case 6:
                delbeg();
                break;
            case 7:
                delend();
                break;
            case 8:
                delpos();
                break;
        }
        printf("\n");
    }
    return 0;
}
