// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_interfaces:msg/NumForTest.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__MSG__DETAIL__NUM_FOR_TEST__BUILDER_HPP_
#define MY_INTERFACES__MSG__DETAIL__NUM_FOR_TEST__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_interfaces/msg/detail/num_for_test__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_interfaces
{

namespace msg
{

namespace builder
{

class Init_NumForTest_random_number
{
public:
  Init_NumForTest_random_number()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_interfaces::msg::NumForTest random_number(::my_interfaces::msg::NumForTest::_random_number_type arg)
  {
    msg_.random_number = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::msg::NumForTest msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::msg::NumForTest>()
{
  return my_interfaces::msg::builder::Init_NumForTest_random_number();
}

}  // namespace my_interfaces

#endif  // MY_INTERFACES__MSG__DETAIL__NUM_FOR_TEST__BUILDER_HPP_
