import wp_func

heading_one = "This is title"

frist_paragraph = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book"

heading_two = 'Where does it come from?'
second_paragraph = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old."

heading_three = 'Why do we use it?'

third_paragraph = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English."
heading_four = "Why do we use it?"
article = wp_func.wp_p(frist_paragraph) + wp_func.wp_h2(heading_two) + wp_func.wp_p(second_paragraph) + wp_func.wp_h3(heading_three) + wp_func.wp_p(third_paragraph) + wp_func.wp_h4(heading_four)

print(article)