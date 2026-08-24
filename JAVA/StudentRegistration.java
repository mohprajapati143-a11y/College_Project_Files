import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class StudentRegistration extends JFrame implements ActionListener {

    JTextField name, email, phone;
    JRadioButton male, female;
    JComboBox<String> course;
    JCheckBox java, python, dbms;
    JTextArea address;
    JButton submit, clear;

    StudentRegistration() {

        setTitle("Student Registration");
        setSize(450, 500);
        setLayout(new GridLayout(9, 2, 5, 5));

        add(new JLabel("Name:"));
        name = new JTextField();
        add(name);

        add(new JLabel("Email:"));
        email = new JTextField();
        add(email);

        add(new JLabel("Phone:"));
        phone = new JTextField();
        add(phone);

        add(new JLabel("Gender:"));

        JPanel p = new JPanel();

        male = new JRadioButton("Male");
        female = new JRadioButton("Female");

        ButtonGroup bg = new ButtonGroup();
        bg.add(male);
        bg.add(female);

        p.add(male);
        p.add(female);

        add(p);

        add(new JLabel("Course:"));

        course = new JComboBox<>(
                new String[]{"BCA", "BSc IT", "BSc CS", "B.Tech"}
        );

        add(course);

        add(new JLabel("Subjects:"));

        JPanel s = new JPanel();

        java = new JCheckBox("Java");
        python = new JCheckBox("Python");
        dbms = new JCheckBox("DBMS");

        s.add(java);
        s.add(python);
        s.add(dbms);

        add(s);

        add(new JLabel("Address:"));

        address = new JTextArea(3, 20);
        add(new JScrollPane(address));

        submit = new JButton("Submit");
        clear = new JButton("Clear");

        submit.addActionListener(this);
        clear.addActionListener(this);

        add(submit);
        add(clear);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {

        if (e.getSource() == submit) {

            JOptionPane.showMessageDialog(
                    this,
                    "Registration Successful!\nWelcome "
                            + name.getText()
            );
        }

        if (e.getSource() == clear) {

            name.setText("");
            email.setText("");
            phone.setText("");
            address.setText("");

            java.setSelected(false);
            python.setSelected(false);
            dbms.setSelected(false);
        }
    }

    public static void main(String[] args) {

        new StudentRegistration();
    }
}