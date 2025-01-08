// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_interfaces:msg/SensorStatus.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__MSG__DETAIL__SENSOR_STATUS__STRUCT_H_
#define MY_INTERFACES__MSG__DETAIL__SENSOR_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'debug_messages'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/SensorStatus in the package my_interfaces.
typedef struct my_interfaces__msg__SensorStatus
{
  int64_t temerature;
  bool is_motor_ready;
  rosidl_runtime_c__String debug_messages;
} my_interfaces__msg__SensorStatus;

// Struct for a sequence of my_interfaces__msg__SensorStatus.
typedef struct my_interfaces__msg__SensorStatus__Sequence
{
  my_interfaces__msg__SensorStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_interfaces__msg__SensorStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_INTERFACES__MSG__DETAIL__SENSOR_STATUS__STRUCT_H_
