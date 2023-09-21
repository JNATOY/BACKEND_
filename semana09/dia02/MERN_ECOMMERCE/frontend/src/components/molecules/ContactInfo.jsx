const ContactInfo = ()=>{
    return(
        <div className="col-lg-8">
              <ul className="links_list links_list-align-right align-center-desktop topbar-contacts">
                <li>
                  <p className="links_list-label">
                    Nuestra Dirección
                  </p>
                  <p className="links_list-value">
                    <a href="http://maps.google.com">Av la marina 135, San Miguel</a>
                  </p>
                </li>
                <li>
                  <p className="links_list-label">
                    Contactanos
                  </p>
                  <p className="links_list-value">
                    <a href="mailto:support@email.com">Support@Email.com</a>
                  </p>
                </li>
                <li>
                  <p className="links_list-label">
                    Telefono
                  </p>
                  <p className="links_list-value">
                    <a href="tel:4785929899">(478)-592-9899</a>
                  </p>
                </li>
              </ul>
            </div>
    )
}

export default ContactInfo