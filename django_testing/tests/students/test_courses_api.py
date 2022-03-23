import pytest
from rest_framework.reverse import reverse
# from django.urls import reverse
from rest_framework.test import APIClient
from students.models import Student, Course
from model_bakery import baker


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def students_factory():
    def factory_student(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory_student


@pytest.fixture
def courses_factory():
    def factory_course(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory_course




# @pytest.mark.django_db
# def test_get_one_course(client, courses_factory):
#     courses_l = courses_factory(_quantity=10)
#     url = reverse('courses-list')
#     response = client.get(url)
#     data = response.json()
#     assert response.status_code == 200
#     assert courses_l[0].id == data[0]['id']
#     assert courses_l[0].name == data[0]['name']
#
#
#
# @pytest.mark.django_db
# def test_get_list_courses(client, courses_factory):
#     courses_l = courses_factory(_quantity=10)
#     url = reverse('courses-list')
#     response = client.get(url)
#     data = response.json()
#     assert response.status_code == 200
#     assert len(courses_l) == len(data)
#     for i in range(10):
#         assert courses_l[i].id == data[i]['id']
#         assert courses_l[i].name == data[i]['name']


# @pytest.mark.django_db
# def test_get_course_filter_id(client, courses_factory):
#     courses_l = courses_factory(_quantity=10)
#     url = reverse('courses-list')
#     response = client.get(url, {'id': 1})
#     data = response.json()
#     print("data -", data[0]['id'])
#     assert response.status_code == 200
#     assert data[0]['id'] == 1


# @pytest.mark.django_db
# def test_get_course_filter_name(client, courses_factory):
#     courses_l = courses_factory(_quantity=10)
#     url = reverse('courses-list')
#     response = client.get(url, {'name': courses_l[0].name})
#     data = response.json()
#     print("data -", data[0]['id'])
#     assert response.status_code == 200
#     assert data[0]['name'] == courses_l[0].name

# @pytest.mark.django_db
# def test_sreate_course(client):
#     data = {
#         'name': 'super_course',
#         'students_id': 1
#     }
#     url = reverse('courses-list')
#     response = client.post(url, data=data)
#     assert response.status_code == 201




@pytest.mark.django_db
def test_patch_course(client, courses_factory):
    course = courses_factory(_quantity=1)
    data = {
        'name': 'super_course'
    }
    url = reverse('courses-list')
    print("url -", url)
    response = client.patch(url, data=data)
    print(response)
    data = response.json()
    assert response.status_code == 200