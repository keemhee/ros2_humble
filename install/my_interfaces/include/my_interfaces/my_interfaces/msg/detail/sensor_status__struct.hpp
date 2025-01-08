// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_interfaces:msg/SensorStatus.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__MSG__DETAIL__SENSOR_STATUS__STRUCT_HPP_
#define MY_INTERFACES__MSG__DETAIL__SENSOR_STATUS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_interfaces__msg__SensorStatus __attribute__((deprecated))
#else
# define DEPRECATED__my_interfaces__msg__SensorStatus __declspec(deprecated)
#endif

namespace my_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct SensorStatus_
{
  using Type = SensorStatus_<ContainerAllocator>;

  explicit SensorStatus_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->temerature = 0ll;
      this->is_motor_ready = false;
      this->debug_messages = "";
    }
  }

  explicit SensorStatus_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : debug_messages(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->temerature = 0ll;
      this->is_motor_ready = false;
      this->debug_messages = "";
    }
  }

  // field types and members
  using _temerature_type =
    int64_t;
  _temerature_type temerature;
  using _is_motor_ready_type =
    bool;
  _is_motor_ready_type is_motor_ready;
  using _debug_messages_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _debug_messages_type debug_messages;

  // setters for named parameter idiom
  Type & set__temerature(
    const int64_t & _arg)
  {
    this->temerature = _arg;
    return *this;
  }
  Type & set__is_motor_ready(
    const bool & _arg)
  {
    this->is_motor_ready = _arg;
    return *this;
  }
  Type & set__debug_messages(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->debug_messages = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_interfaces::msg::SensorStatus_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_interfaces::msg::SensorStatus_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_interfaces::msg::SensorStatus_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_interfaces::msg::SensorStatus_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_interfaces::msg::SensorStatus_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::msg::SensorStatus_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_interfaces::msg::SensorStatus_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::msg::SensorStatus_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_interfaces::msg::SensorStatus_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_interfaces::msg::SensorStatus_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_interfaces__msg__SensorStatus
    std::shared_ptr<my_interfaces::msg::SensorStatus_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_interfaces__msg__SensorStatus
    std::shared_ptr<my_interfaces::msg::SensorStatus_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SensorStatus_ & other) const
  {
    if (this->temerature != other.temerature) {
      return false;
    }
    if (this->is_motor_ready != other.is_motor_ready) {
      return false;
    }
    if (this->debug_messages != other.debug_messages) {
      return false;
    }
    return true;
  }
  bool operator!=(const SensorStatus_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SensorStatus_

// alias to use template instance with default allocator
using SensorStatus =
  my_interfaces::msg::SensorStatus_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace my_interfaces

#endif  // MY_INTERFACES__MSG__DETAIL__SENSOR_STATUS__STRUCT_HPP_
