// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from my_interfaces:action/Move.idl
// generated code does not contain a copyright notice

#ifndef MY_INTERFACES__ACTION__DETAIL__MOVE__BUILDER_HPP_
#define MY_INTERFACES__ACTION__DETAIL__MOVE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "my_interfaces/action/detail/move__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace my_interfaces
{

namespace action
{

namespace builder
{

class Init_Move_Goal_distance
{
public:
  Init_Move_Goal_distance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_interfaces::action::Move_Goal distance(::my_interfaces::action::Move_Goal::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::action::Move_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::action::Move_Goal>()
{
  return my_interfaces::action::builder::Init_Move_Goal_distance();
}

}  // namespace my_interfaces


namespace my_interfaces
{

namespace action
{

namespace builder
{

class Init_Move_Result_total_distance
{
public:
  Init_Move_Result_total_distance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_interfaces::action::Move_Result total_distance(::my_interfaces::action::Move_Result::_total_distance_type arg)
  {
    msg_.total_distance = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::action::Move_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::action::Move_Result>()
{
  return my_interfaces::action::builder::Init_Move_Result_total_distance();
}

}  // namespace my_interfaces


namespace my_interfaces
{

namespace action
{

namespace builder
{

class Init_Move_Feedback_current_distance
{
public:
  Init_Move_Feedback_current_distance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_interfaces::action::Move_Feedback current_distance(::my_interfaces::action::Move_Feedback::_current_distance_type arg)
  {
    msg_.current_distance = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::action::Move_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::action::Move_Feedback>()
{
  return my_interfaces::action::builder::Init_Move_Feedback_current_distance();
}

}  // namespace my_interfaces


namespace my_interfaces
{

namespace action
{

namespace builder
{

class Init_Move_SendGoal_Request_goal
{
public:
  explicit Init_Move_SendGoal_Request_goal(::my_interfaces::action::Move_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::my_interfaces::action::Move_SendGoal_Request goal(::my_interfaces::action::Move_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::action::Move_SendGoal_Request msg_;
};

class Init_Move_SendGoal_Request_goal_id
{
public:
  Init_Move_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Move_SendGoal_Request_goal goal_id(::my_interfaces::action::Move_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Move_SendGoal_Request_goal(msg_);
  }

private:
  ::my_interfaces::action::Move_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::action::Move_SendGoal_Request>()
{
  return my_interfaces::action::builder::Init_Move_SendGoal_Request_goal_id();
}

}  // namespace my_interfaces


namespace my_interfaces
{

namespace action
{

namespace builder
{

class Init_Move_SendGoal_Response_stamp
{
public:
  explicit Init_Move_SendGoal_Response_stamp(::my_interfaces::action::Move_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::my_interfaces::action::Move_SendGoal_Response stamp(::my_interfaces::action::Move_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::action::Move_SendGoal_Response msg_;
};

class Init_Move_SendGoal_Response_accepted
{
public:
  Init_Move_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Move_SendGoal_Response_stamp accepted(::my_interfaces::action::Move_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_Move_SendGoal_Response_stamp(msg_);
  }

private:
  ::my_interfaces::action::Move_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::action::Move_SendGoal_Response>()
{
  return my_interfaces::action::builder::Init_Move_SendGoal_Response_accepted();
}

}  // namespace my_interfaces


namespace my_interfaces
{

namespace action
{

namespace builder
{

class Init_Move_GetResult_Request_goal_id
{
public:
  Init_Move_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::my_interfaces::action::Move_GetResult_Request goal_id(::my_interfaces::action::Move_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::action::Move_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::action::Move_GetResult_Request>()
{
  return my_interfaces::action::builder::Init_Move_GetResult_Request_goal_id();
}

}  // namespace my_interfaces


namespace my_interfaces
{

namespace action
{

namespace builder
{

class Init_Move_GetResult_Response_result
{
public:
  explicit Init_Move_GetResult_Response_result(::my_interfaces::action::Move_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::my_interfaces::action::Move_GetResult_Response result(::my_interfaces::action::Move_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::action::Move_GetResult_Response msg_;
};

class Init_Move_GetResult_Response_status
{
public:
  Init_Move_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Move_GetResult_Response_result status(::my_interfaces::action::Move_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_Move_GetResult_Response_result(msg_);
  }

private:
  ::my_interfaces::action::Move_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::action::Move_GetResult_Response>()
{
  return my_interfaces::action::builder::Init_Move_GetResult_Response_status();
}

}  // namespace my_interfaces


namespace my_interfaces
{

namespace action
{

namespace builder
{

class Init_Move_FeedbackMessage_feedback
{
public:
  explicit Init_Move_FeedbackMessage_feedback(::my_interfaces::action::Move_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::my_interfaces::action::Move_FeedbackMessage feedback(::my_interfaces::action::Move_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::my_interfaces::action::Move_FeedbackMessage msg_;
};

class Init_Move_FeedbackMessage_goal_id
{
public:
  Init_Move_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Move_FeedbackMessage_feedback goal_id(::my_interfaces::action::Move_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Move_FeedbackMessage_feedback(msg_);
  }

private:
  ::my_interfaces::action::Move_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::my_interfaces::action::Move_FeedbackMessage>()
{
  return my_interfaces::action::builder::Init_Move_FeedbackMessage_goal_id();
}

}  // namespace my_interfaces

#endif  // MY_INTERFACES__ACTION__DETAIL__MOVE__BUILDER_HPP_
