// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_interfaces:msg/SensorStatus.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__MSG__DETAIL__SENSOR_STATUS__TRAITS_HPP_
#define MY_INTERFACES__MSG__DETAIL__SENSOR_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "my_interfaces/msg/detail/sensor_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace my_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const SensorStatus & msg,
  std::ostream & out)
{
  out << "{";
  // member: temerature
  {
    out << "temerature: ";
    rosidl_generator_traits::value_to_yaml(msg.temerature, out);
    out << ", ";
  }

  // member: is_motor_ready
  {
    out << "is_motor_ready: ";
    rosidl_generator_traits::value_to_yaml(msg.is_motor_ready, out);
    out << ", ";
  }

  // member: debug_messages
  {
    out << "debug_messages: ";
    rosidl_generator_traits::value_to_yaml(msg.debug_messages, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SensorStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: temerature
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "temerature: ";
    rosidl_generator_traits::value_to_yaml(msg.temerature, out);
    out << "\n";
  }

  // member: is_motor_ready
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_motor_ready: ";
    rosidl_generator_traits::value_to_yaml(msg.is_motor_ready, out);
    out << "\n";
  }

  // member: debug_messages
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "debug_messages: ";
    rosidl_generator_traits::value_to_yaml(msg.debug_messages, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SensorStatus & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace my_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use my_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const my_interfaces::msg::SensorStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  my_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use my_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const my_interfaces::msg::SensorStatus & msg)
{
  return my_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<my_interfaces::msg::SensorStatus>()
{
  return "my_interfaces::msg::SensorStatus";
}

template<>
inline const char * name<my_interfaces::msg::SensorStatus>()
{
  return "my_interfaces/msg/SensorStatus";
}

template<>
struct has_fixed_size<my_interfaces::msg::SensorStatus>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<my_interfaces::msg::SensorStatus>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<my_interfaces::msg::SensorStatus>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MY_INTERFACES__MSG__DETAIL__SENSOR_STATUS__TRAITS_HPP_
