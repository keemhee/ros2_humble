// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_interfaces:msg/SensorStatus.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__MSG__DETAIL__SENSOR_STATUS__BUILDER_HPP_
#define MY_INTERFACES__MSG__DETAIL__SENSOR_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_interfaces/msg/detail/sensor_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_interfaces
{

namespace msg
{

namespace builder
{

class Init_SensorStatus_debug_messages
{
public:
  explicit Init_SensorStatus_debug_messages(::my_interfaces::msg::SensorStatus & msg)
  : msg_(msg)
  {}
  ::my_interfaces::msg::SensorStatus debug_messages(::my_interfaces::msg::SensorStatus::_debug_messages_type arg)
  {
    msg_.debug_messages = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::msg::SensorStatus msg_;
};

class Init_SensorStatus_is_motor_ready
{
public:
  explicit Init_SensorStatus_is_motor_ready(::my_interfaces::msg::SensorStatus & msg)
  : msg_(msg)
  {}
  Init_SensorStatus_debug_messages is_motor_ready(::my_interfaces::msg::SensorStatus::_is_motor_ready_type arg)
  {
    msg_.is_motor_ready = std::move(arg);
    return Init_SensorStatus_debug_messages(msg_);
  }

private:
  ::my_interfaces::msg::SensorStatus msg_;
};

class Init_SensorStatus_temerature
{
public:
  Init_SensorStatus_temerature()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SensorStatus_is_motor_ready temerature(::my_interfaces::msg::SensorStatus::_temerature_type arg)
  {
    msg_.temerature = std::move(arg);
    return Init_SensorStatus_is_motor_ready(msg_);
  }

private:
  ::my_interfaces::msg::SensorStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::msg::SensorStatus>()
{
  return my_interfaces::msg::builder::Init_SensorStatus_temerature();
}

}  // namespace my_interfaces

#endif  // MY_INTERFACES__MSG__DETAIL__SENSOR_STATUS__BUILDER_HPP_
