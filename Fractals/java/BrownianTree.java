//# -*- coding: utf-8 -*- #
// awt (stands for?) imports
import java.awt.Graphics;
import java.awt.image.BufferedImage;
// import std util set
import java.util.*;
// import javax swing JFrame (exposes?)
import javax.swing.JFrame;

// declare BronianTree class and extend JFrame and implement Runnable
public class BrownianTree extends JFrame implements Runnable {

    // Create image Buffer Capital i
    BufferedImage I;
    // Explain what the private statement does. (This creates a List of type Particle called particles)
    private List<Particle> particles;
    // Explain the static statement. (this creates a static var called rand of type Random with the contents of object Random())
    static Random rand = new Random();

    // Declare new function called BrownianTree - no return, no params
    public BrownianTree() {
        // ?
        super("Brownian Tree");
        // Set the bounds of
        setBounds(100, 100, 400, 300);
        // As it says on the tin, setDefaultCloseOperation -> Exit on Close
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        // put a new BufferedImage of size getWidth() and getHeight() into I - The BufferedImage type is int RGB
        I = new BufferedImage(getWidth(), getHeight(), BufferedImage.TYPE_INT_RGB);
        // set I's RGB property to 1/2 the width and 1/2 the height, 0xff00
        I.setRGB(I.getWidth() / 2, I.getHeight() / 2, 0xff00);
        // populate the particles variable with a LinkedList of type Particle
        particles = new LinkedList<Particle>();
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
        // For 20k iterations add a new Particle object to the particles variable.
        for (int i = 0; i < 20000; i++) {
            particles.add(new Particle());
        }
        while (!particles.isEmpty()) {
            for (Iterator<Particle> it = particles.iterator(); it.hasNext();) {
                if (it.next().move()) {
                    it.remove();
                }
            }
            repaint();
        }
    }

    public static void main(String[] args) {
        BrownianTree b = new BrownianTree();
        b.setVisible(true);
        new Thread(b).start();
    }

    private class Particle {

        private int x, y;

        private Particle() {
            x = rand.nextInt(I.getWidth());
            y = rand.nextInt(I.getHeight());
        }

        /* returns true if either out of bounds or collided with tree */
        private boolean move() {
            int dx = rand.nextInt(3) - 1;
            int dy = rand.nextInt(3) - 1;
            if ((x + dx < 0) || (y + dy < 0)
                    || (y + dy >= I.getHeight()) || (x + dx >= I.getWidth())) {
                return true;
            }
            x += dx;
            y += dy;
            if ((I.getRGB(x, y) & 0xff00) == 0xff00) {
                I.setRGB(x - dx, y - dy, 0xff00);
                return true;
            }
            return false;
        }
    }
}