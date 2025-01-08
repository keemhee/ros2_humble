// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from my_interfaces:srv/Move.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__MOVE__STRUCT_HPP_
#define MY_INTERFACES__SRV__DETAIL__MOVE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__my_interfaces__srv__Move_Request __attribute__((deprecated))
#else
# define DEPRECATED__my_interfaces__srv__Move_Request __declspec(deprecated)
#endif

namespace my_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Move_Request_
{
  using Type = Move_Request_<ContainerAllocator>;

  explicit Move_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->linear_velocity = 0.0f;
      this->angular_velocity = 0.0f;
    }
  }

  explicit Move_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->linear_velocity = 0.0f;
      this->angular_velocity = 0.0f;
    }
  }

  // field types and members
  using _linear_velocity_type =
    float;
  _linear_velocity_type linear_velocity;
  using _angular_velocity_type =
    float;
  _angular_velocity_type angular_velocity;

  // setters for named parameter idiom
  Type & set__linear_velocity(
    const float & _arg)
  {
    this->linear_velocity = _arg;
    return *this;
  }
  Type & set__angular_velocity(
    const float & _arg)
  {
    this->angular_velocity = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_interfaces::srv::Move_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_interfaces::srv::Move_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_interfaces::srv::Move_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_interfaces::srv::Move_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Move_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Move_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Move_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Move_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_interfaces::srv::Move_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_interfaces::srv::Move_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_interfaces__srv__Move_Request
    std::shared_ptr<my_interfaces::srv::Move_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_interfaces__srv__Move_Request
    std::shared_ptr<my_interfaces::srv::Move_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Move_Request_ & other) const
  {
    if (this->linear_velocity != other.linear_velocity) {
      return false;
    }
    if (this->angular_velocity != other.angular_velocity) {
      return false;
    }
    return true;
  }
  bool operator!=(const Move_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Move_Request_

// alias to use template instance with default allocator
using Move_Request =
  my_interfaces::srv::Move_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_interfaces


#ifndef _WIN32
# define DEPRECATED__my_interfaces__srv__Move_Response __attribute__((deprecated))
#else
# define DEPRECATED__my_interfaces__srv__Move_Response __declspec(deprecated)
#endif

namespace my_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Move_Response_
{
  using Type = Move_Response_<ContainerAllocator>;

  explicit Move_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  explicit Move_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _message_type message;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__message(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->message = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    my_interfaces::srv::Move_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const my_interfaces::srv::Move_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<my_interfaces::srv::Move_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<my_interfaces::srv::Move_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Move_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Move_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      my_interfaces::srv::Move_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<my_interfaces::srv::Move_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<my_interfaces::srv::Move_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<my_interfaces::srv::Move_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__my_interfaces__srv__Move_Response
    std::shared_ptr<my_interfaces::srv::Move_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__my_interfaces__srv__Move_Response
    std::shared_ptr<my_interfaces::srv::Move_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Move_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->message != other.message) {
      return false;
    }
    return true;
  }
  bool operator!=(const Move_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Move_Response_

// alias to use template instance with default allocator
using Move_Response =
  my_interfaces::srv::Move_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace my_interfaces

namespace my_interfaces
{

namespace srv
{

struct Move
{
  using Request = my_interfaces::srv::Move_Request;
  using Response = my_interfaces::srv::Move_Response;
};

}  // namespace srv

}  // namespace my_interfaces

#endif  // MY_INTERFACES__SRV__DETAIL__MOVE__STRUCT_HPP_
