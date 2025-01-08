// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from my_interfaces:msg/NumForTest.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__MSG__DETAIL__NUM_FOR_TEST__FUNCTIONS_H_
#define MY_INTERFACES__MSG__DETAIL__NUM_FOR_TEST__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "my_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "my_interfaces/msg/detail/num_for_test__struct.h"

/// Initialize msg/NumForTest message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * my_interfaces__msg__NumForTest
 * )) before or use
 * my_interfaces__msg__NumForTest__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_my_interfaces
bool
my_interfaces__msg__NumForTest__init(my_interfaces__msg__NumForTest * msg);

/// Finalize msg/NumForTest message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_interfaces
void
my_interfaces__msg__NumForTest__fini(my_interfaces__msg__NumForTest * msg);

/// Create msg/NumForTest message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * my_interfaces__msg__NumForTest__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_my_interfaces
my_interfaces__msg__NumForTest *
my_interfaces__msg__NumForTest__create();

/// Destroy msg/NumForTest message.
/**
 * It calls
 * my_interfaces__msg__NumForTest__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_interfaces
void
my_interfaces__msg__NumForTest__destroy(my_interfaces__msg__NumForTest * msg);

/// Check for msg/NumForTest message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_interfaces
bool
my_interfaces__msg__NumForTest__are_equal(const my_interfaces__msg__NumForTest * lhs, const my_interfaces__msg__NumForTest * rhs);

/// Copy a msg/NumForTest message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_interfaces
bool
my_interfaces__msg__NumForTest__copy(
  const my_interfaces__msg__NumForTest * input,
  my_interfaces__msg__NumForTest * output);

/// Initialize array of msg/NumForTest messages.
/**
 * It allocates the memory for the number of elements and calls
 * my_interfaces__msg__NumForTest__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_interfaces
bool
my_interfaces__msg__NumForTest__Sequence__init(my_interfaces__msg__NumForTest__Sequence * array, size_t size);

/// Finalize array of msg/NumForTest messages.
/**
 * It calls
 * my_interfaces__msg__NumForTest__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_interfaces
void
my_interfaces__msg__NumForTest__Sequence__fini(my_interfaces__msg__NumForTest__Sequence * array);

/// Create array of msg/NumForTest messages.
/**
 * It allocates the memory for the array and calls
 * my_interfaces__msg__NumForTest__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_my_interfaces
my_interfaces__msg__NumForTest__Sequence *
my_interfaces__msg__NumForTest__Sequence__create(size_t size);

/// Destroy array of msg/NumForTest messages.
/**
 * It calls
 * my_interfaces__msg__NumForTest__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_interfaces
void
my_interfaces__msg__NumForTest__Sequence__destroy(my_interfaces__msg__NumForTest__Sequence * array);

/// Check for msg/NumForTest message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_interfaces
bool
my_interfaces__msg__NumForTest__Sequence__are_equal(const my_interfaces__msg__NumForTest__Sequence * lhs, const my_interfaces__msg__NumForTest__Sequence * rhs);

/// Copy an array of msg/NumForTest messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_my_interfaces
bool
my_interfaces__msg__NumForTest__Sequence__copy(
  const my_interfaces__msg__NumForTest__Sequence * input,
  my_interfaces__msg__NumForTest__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // MY_INTERFACES__MSG__DETAIL__NUM_FOR_TEST__FUNCTIONS_H_
