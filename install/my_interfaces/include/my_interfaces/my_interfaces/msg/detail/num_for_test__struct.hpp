// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_interfaces:msg/NumForTest.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__MSG__DETAIL__NUM_FOR_TEST__STRUCT_HPP_
#define MY_INTERFACES__MSG__DETAIL__NUM_FOR_TEST__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_interfaces__msg__NumForTest __attribute__((deprecated))
#else
# define DEPRECATED__my_interfaces__msg__NumForTest __declspec(deprecated)
#endif

namespace my_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct NumForTest_
{
  using Type = NumForTest_<ContainerAllocator>;

  explicit NumForTest_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->random_number = 0ll;
    }
  }

  explicit NumForTest_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->random_number = 0ll;
    }
  }

  // field types and members
  using _random_number_type =
    int64_t;
  _random_number_type random_number;

  // setters for named parameter idiom
  Type & set__random_number(
    const int64_t & _arg)
  {
    this->random_number = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_interfaces::msg::NumForTest_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_interfaces::msg::NumForTest_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_interfaces::msg::NumForTest_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_interfaces::msg::NumForTest_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_interfaces::msg::NumForTest_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::msg::NumForTest_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_interfaces::msg::NumForTest_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::msg::NumForTest_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_interfaces::msg::NumForTest_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_interfaces::msg::NumForTest_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_interfaces__msg__NumForTest
    std::shared_ptr<my_interfaces::msg::NumForTest_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_interfaces__msg__NumForTest
    std::shared_ptr<my_interfaces::msg::NumForTest_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const NumForTest_ & other) const
  {
    if (this->random_number != other.random_number) {
      return false;
    }
    return true;
  }
  bool operator!=(const NumForTest_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct NumForTest_

// alias to use template instance with default allocator
using NumForTest =
  my_interfaces::msg::NumForTest_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace my_interfaces

#endif  // MY_INTERFACES__MSG__DETAIL__NUM_FOR_TEST__STRUCT_HPP_
