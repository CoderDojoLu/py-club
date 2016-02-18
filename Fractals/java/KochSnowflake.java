import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.util.*;
import javax.swing.JFrame;

public class KochSnowflake extends JFrame implements Runnable {

    BufferedImage I;

    public KochSnowflake() {
        // ?
        super("Koch Snowflake");
        // Set the bounds of
        setBounds(100, 100, 400, 300);
        // As it says on the tin, setDefaultCloseOperation -> Exit on Close
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        // put a new BufferedImage of size getWidth() and getHeight() into I - The BufferedImage type is int RGB
        I = new BufferedImage(getWidth(), getHeight(), BufferedImage.TYPE_INT_RGB);
        // set I's RGB property to 1/2 the width and 1/2 the height, 0xff00
        I.setRGB(I.getWidth() / 2, I.getHeight() / 2, 0xff00);
        // populate the particles variable with a LinkedList of type Particle
    }


    // Override function paint
    @Override
    // paint returns void (nothing) and has a parameter g of type Graphics
    public void paint(Graphics g) {
        // draw Image I
        g.drawImage(I, 0, 0, this);
    }
        // override run
    public void run() {
        repaint();
    }

    public static void main(String[] args) {
    KochSnowflake b = new KochSnowflake();
    b.setVisible(true);
    new Thread(b).start();
   }


  }