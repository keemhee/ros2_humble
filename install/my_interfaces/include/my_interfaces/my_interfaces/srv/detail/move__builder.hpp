// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_interfaces:srv/Move.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__SRV__DETAIL__MOVE__BUILDER_HPP_
#define MY_INTERFACES__SRV__DETAIL__MOVE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_interfaces/srv/detail/move__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_interfaces
{

namespace srv
{

namespace builder
{

class Init_Move_Request_angular_velocity
{
public:
  explicit Init_Move_Request_angular_velocity(::my_interfaces::srv::Move_Request & msg)
  : msg_(msg)
  {}
  ::my_interfaces::srv::Move_Request angular_velocity(::my_interfaces::srv::Move_Request::_angular_velocity_type arg)
  {
    msg_.angular_velocity = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::srv::Move_Request msg_;
};

class Init_Move_Request_linear_velocity
{
public:
  Init_Move_Request_linear_velocity()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Move_Request_angular_velocity linear_velocity(::my_interfaces::srv::Move_Request::_linear_velocity_type arg)
  {
    msg_.linear_velocity = std::move(arg);
    return Init_Move_Request_angular_velocity(msg_);
  }

private:
  ::my_interfaces::srv::Move_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::srv::Move_Request>()
{
  return my_interfaces::srv::builder::Init_Move_Request_linear_velocity();
}

}  // namespace my_interfaces


namespace my_interfaces
{

namespace srv
{

namespace builder
{

class Init_Move_Response_message
{
public:
  explicit Init_Move_Response_message(::my_interfaces::srv::Move_Response & msg)
  : msg_(msg)
  {}
  ::my_interfaces::srv::Move_Response message(::my_interfaces::srv::Move_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::srv::Move_Response msg_;
};

class Init_Move_Response_success
{
public:
  Init_Move_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Move_Response_message success(::my_interfaces::srv::Move_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_Move_Response_message(msg_);
  }

private:
  ::my_interfaces::srv::Move_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::srv::Move_Response>()
{
  return my_interfaces::srv::builder::Init_Move_Response_success();
}

}  // namespace my_interfaces

#endif  // MY_INTERFACES__SRV__DETAIL__MOVE__BUILDER_HPP_
