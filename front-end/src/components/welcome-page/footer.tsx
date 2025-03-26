import "../../styles/footer.css";

const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="column">
          <h4>For Clients</h4>
          <ul>
            <li><a href="#">How to hire</a></li>
            <li><a href="#">Talent Marketplace</a></li>
            <li><a href="#">Project Catalog</a></li>
            <li><a href="#">Hire an agency</a></li>
            <li><a href="#">Enterprise</a></li>
            <li><a href="#">Business Plus</a></li>
          </ul>
        </div>

        <div className="column">
          <h4>For Talent</h4>
          <ul>
            <li><a href="#">How to find work</a></li>
            <li><a href="#">Direct Contracts</a></li>
            <li><a href="#">Find freelance jobs worldwide</a></li>
            <li><a href="#">Find freelance jobs in the USA</a></li>
            <li><a href="#">Win work with ads</a></li>
          </ul>
        </div>

        <div className="column">
          <h4>Resources</h4>
          <ul>
            <li><a href="#">Help & support</a></li>
            <li><a href="#">Success stories</a></li>
            <li><a href="#">Upwork reviews</a></li>
            <li><a href="#">Resources</a></li>
            <li><a href="#">Blog</a></li>
          </ul>
        </div>

        <div className="column">
          <h4>Company</h4>
          <ul>
            <li><a href="#">About us</a></li>
            <li><a href="#">Leadership</a></li>
            <li><a href="#">Investor relations</a></li>
            <li><a href="#">Careers</a></li>
            <li><a href="#">Our impact</a></li>
          </ul>
        </div>
      </div>

      {/* Нижні посилання */}
      <div className="footer-bottom">
        <ul>
          <li><a href="#">Terms of Service</a></li>
          <li><a href="#">Privacy Policy</a></li>
          <li><a href="#">CA Notice at Collection</a></li>
          <li><a href="#">Cookie Settings</a></li>
          <li><a href="#">Accessibility</a></li>
        </ul>
      </div>
    </footer>
  );
};

export default Footer;
