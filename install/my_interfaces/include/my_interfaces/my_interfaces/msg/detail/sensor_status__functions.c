// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from my_interfaces:msg/SensorStatus.idl
// generated code does not contain a copyright notice
#include "my_interfaces/msg/detail/sensor_status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `debug_messages`
#include "rosidl_runtime_c/string_functions.h"

bool
my_interfaces__msg__SensorStatus__init(my_interfaces__msg__SensorStatus * msg)
{
  if (!msg) {
    return false;
  }
  // temerature
  // is_motor_ready
  // debug_messages
  if (!rosidl_runtime_c__String__init(&msg->debug_messages)) {
    my_interfaces__msg__SensorStatus__fini(msg);
    return false;
  }
  return true;
}

void
my_interfaces__msg__SensorStatus__fini(my_interfaces__msg__SensorStatus * msg)
{
  if (!msg) {
    return;
  }
  // temerature
  // is_motor_ready
  // debug_messages
  rosidl_runtime_c__String__fini(&msg->debug_messages);
}

bool
my_interfaces__msg__SensorStatus__are_equal(const my_interfaces__msg__SensorStatus * lhs, const my_interfaces__msg__SensorStatus * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // temerature
  if (lhs->temerature != rhs->temerature) {
    return false;
  }
  // is_motor_ready
  if (lhs->is_motor_ready != rhs->is_motor_ready) {
    return false;
  }
  // debug_messages
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->debug_messages), &(rhs->debug_messages)))
  {
    return false;
  }
  return true;
}

bool
my_interfaces__msg__SensorStatus__copy(
  const my_interfaces__msg__SensorStatus * input,
  my_interfaces__msg__SensorStatus * output)
{
  if (!input || !output) {
    return false;
  }
  // temerature
  output->temerature = input->temerature;
  // is_motor_ready
  output->is_motor_ready = input->is_motor_ready;
  // debug_messages
  if (!rosidl_runtime_c__String__copy(
      &(input->debug_messages), &(output->debug_messages)))
  {
    return false;
  }
  return true;
}

my_interfaces__msg__SensorStatus *
my_interfaces__msg__SensorStatus__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_interfaces__msg__SensorStatus * msg = (my_interfaces__msg__SensorStatus *)allocator.allocate(sizeof(my_interfaces__msg__SensorStatus), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(my_interfaces__msg__SensorStatus));
  bool success = my_interfaces__msg__SensorStatus__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
my_interfaces__msg__SensorStatus__destroy(my_interfaces__msg__SensorStatus * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    my_interfaces__msg__SensorStatus__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
my_interfaces__msg__SensorStatus__Sequence__init(my_interfaces__msg__SensorStatus__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_interfaces__msg__SensorStatus * data = NULL;

  if (size) {
    data = (my_interfaces__msg__SensorStatus *)allocator.zero_allocate(size, sizeof(my_interfaces__msg__SensorStatus), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = my_interfaces__msg__SensorStatus__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        my_interfaces__msg__SensorStatus__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
my_interfaces__msg__SensorStatus__Sequence__fini(my_interfaces__msg__SensorStatus__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      my_interfaces__msg__SensorStatus__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

my_interfaces__msg__SensorStatus__Sequence *
my_interfaces__msg__SensorStatus__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  my_interfaces__msg__SensorStatus__Sequence * array = (my_interfaces__msg__SensorStatus__Sequence *)allocator.allocate(sizeof(my_interfaces__msg__SensorStatus__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = my_interfaces__msg__SensorStatus__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
my_interfaces__msg__SensorStatus__Sequence__destroy(my_interfaces__msg__SensorStatus__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    my_interfaces__msg__SensorStatus__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
my_interfaces__msg__SensorStatus__Sequence__are_equal(const my_interfaces__msg__SensorStatus__Sequence * lhs, const my_interfaces__msg__SensorStatus__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!my_interfaces__msg__SensorStatus__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
my_interfaces__msg__SensorStatus__Sequence__copy(
  const my_interfaces__msg__SensorStatus__Sequence * input,
  my_interfaces__msg__SensorStatus__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(my_interfaces__msg__SensorStatus);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    my_interfaces__msg__SensorStatus * data =
      (my_interfaces__msg__SensorStatus *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!my_interfaces__msg__SensorStatus__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          my_interfaces__msg__SensorStatus__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!my_interfaces__msg__SensorStatus__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
